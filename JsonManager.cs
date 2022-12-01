// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.Json;
using Gatherer.Types;
using Gatherer.Exporters;
using Gatherer.Formatting;

namespace Gatherer.JsonManager
{
    public class Json
    {
        static JsonSerializerOptions options = new JsonSerializerOptions(JsonSerializerDefaults.Web);

        static public SteamReviews parseJSON(string fileToParse)
        {
            var reviews = JsonSerializer.Deserialize<SteamReviews>(fileToParse, options);   // Deserialize string back to JSON format

            if (reviews != null) { return reviews; }                                        // If it isn't null then it returns it
            return new SteamReviews();                                                      // Otherwise return New Object
        }

        static public SteamReviews combineJSON(DateTime request_time)
        {
            List<Review> allReviews = new List<Review>();                                   // Initializing variables for later use
            SteamReviews mergedReviews = new SteamReviews();                                //

            List<SteamReviews> reports_list = getReports();                                 // Gather Reports previously exported

            foreach (SteamReviews StRev in reports_list)
            {
                allReviews.AddRange(StRev.reviews);                                         // Extracts the reviews of each files and adds them to a list 
            }

            mergedReviews.success = reports_list[0].success;                                // Create new JSON using the variables of 
            mergedReviews.query_summary = reports_list[0].query_summary;                    // first request for some elements and
            mergedReviews.reviews = allReviews;                                             // the final reviews list for the reviews element
            mergedReviews.cursor = "*";

            Export.JSON(JsonSerializer.Serialize(mergedReviews), request_time);             // Exports the final file
            return mergedReviews;                                                           // Writes data to a CSV file
        }

        static private List<SteamReviews> getReports()
        {
            string[] files = Directory.GetFiles("reports/temp/");
            List<SteamReviews> reports_list = new List<SteamReviews>();

            foreach (string file in files)                                      // Goes back through every report exported beforehand
            {
                Console.WriteLine(file);
                string temp = File.ReadAllText(file);                           // Opens the reports as strings
                reports_list.Add(parseJSON(temp));                              // Adds the parsed files to an Array

                File.Delete(file);                                              // Deletes the file
            }

            return reports_list;
        }

        static public List<ReviewSimplified> json2csv(SteamReviews SteamRvws)
        {
            List<Review> reviews = new List<Review>();
            List<ReviewSimplified> csv = new List<ReviewSimplified>();

            foreach (Review rvw in SteamRvws.reviews)
            {
                ReviewSimplified temp = new ReviewSimplified();

                temp.authorID = rvw.author.steamid;
                temp.language = rvw.language;

                temp.review = Format.Text(rvw.review);

                temp.playtime_total = Format.Duration(rvw.author.playtime_forever);
                temp.playtime_last_two_weeks = Format.Duration(rvw.author.playtime_last_two_weeks);
                temp.playtime_at_review = Format.Duration(rvw.author.playtime_at_review);

                temp.review_creation_timestamp = Format.Date(rvw.timestamp_created);
                temp.review_update_timestamp = Format.Date(rvw.timestamp_updated);

                if (rvw.steam_purchase == false) { temp.purchase_type = PurchaseType.NonSteam; }
                else if (rvw.received_for_free == true) { temp.purchase_type = PurchaseType.Free; }
                else { temp.purchase_type = PurchaseType.Paid; }

                csv.Add(temp);
            }

            return csv;
        }
    }
}