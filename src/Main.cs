// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

namespace Gatherer
{
    class Program
    {
        // -------------------------------------------------------------------------------------------------------------------------------------------------------- //
        //                                                                                                                                                          //
        //        **Steam Web API Doc**                                                                                                                             //
        //          https://partner.steamgames.com/doc/store/getreviews                                                                                             //
        //          https://partner.steamgames.com/doc/store/localization/languages                                                                                 //
        //                                                                                                                                                          //
        //                                                                                                                                                          //
        //        **List of Arguments**                                                                                                                             //
        //          App ID ················ 7-digit number used to identify a game                                                                                  //
        //          Filter ················ all | recent | updated ; used to filter gathered reviews by the most recents, the last updated, or by relevance (all)   //
        //          Language ·············· Lang code used to used to filter gathered reviews by languages, codes can be found on the Steam API Doc                 //
        //          Day Range ············· Number ranging from 0-365 ; only reviews sent from today - day range will be gathered (only works with filter:all)      //
        //          Review Type ··········· all | positive | negative ; used to filter gathered reviews by the type of review                                       //
        //          Purchase Type ········· all | non_steam_purchase | steam ; used to filter gathered reviews by where it was purchased                            //
        //          Number of Reviews ····· Number ranging from 1-Infinity ; Total Number of reviews that will be gathered                                          //
        //                                                                                                                                                          //
        // -------------------------------------------------------------------------------------------------------------------------------------------------------- //

        // Private Variables
        static private List<string> arguments = new List<string>(7);
        static private List<APIRequestResult> requestResultAll = new List<APIRequestResult>();
        static private List<Review> reviewsAll = new List<Review>();
        static private List<ReviewSimplified> reviewSimplifiedAll = new List<ReviewSimplified>();
        static private APIRequestResult requestResult = new APIRequestResult();
        static private QuerySummary reportSummary = new QuerySummary();
        static private DateTime requestTime;
        static private string requestURL = "";
        static private string requestCursor = "*";
        static private int reviewPerRequest = 20;
        static private int reviewNumberRemaining = 0;

        static void Main(string[] args)
        {
            Config.ReadConfig();

            arguments = args.ToList();
            requestURL = Web.CreateURL(arguments);
            reviewNumberRemaining = Int16.Parse(arguments[6]);

            requestTime = DateTime.Now;

            while (reviewNumberRemaining > 0)
            {
                requestResult = Web.MakeWebRequest(requestURL, Math.Min(reviewPerRequest, reviewNumberRemaining), requestCursor);

                reviewsAll.AddRange(requestResult.reviews);
                AddQuerySummary(requestResult.query_summary);

                requestCursor = requestResult.cursor;
                reviewNumberRemaining -= reviewPerRequest;
                reviewNumberRemaining = Math.Max(reviewNumberRemaining, 0);

                Thread.Sleep(100);
            }

            requestResult.success = 1;
            requestResult.query_summary = reportSummary;
            requestResult.reviews = reviewsAll;
            requestResult.cursor = "*";

            FileWriter.WriteJSON(Parser.ParseAPIRequestResult(requestResult), Formatter.Date(requestTime));

            foreach (Review reviewTemp in requestResult.reviews)
            {
                reviewSimplifiedAll.Add(Parser.ParseSimplifiedReview(reviewTemp));
            }

            FileWriter.WriteCSV(reviewSimplifiedAll, requestTime);
        }

        static private void AddQuerySummary(QuerySummary summary)
        {
            reportSummary.num_reviews += summary.num_reviews;
            if (reportSummary.review_score_desc == "")
            {
                reportSummary.review_score_desc = summary.review_score_desc;
                reportSummary.total_positive = summary.total_positive;
                reportSummary.total_negative = summary.total_negative;
                reportSummary.total_reviews = summary.total_reviews;
                reportSummary.review_score += summary.review_score;
            }
        }
    }
}