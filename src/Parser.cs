// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.Json;

namespace Gatherer
{
    public class Parser
    {
        static JsonSerializerOptions serializerOptions = new JsonSerializerOptions(JsonSerializerDefaults.Web);

        static public APIRequestResult ParseAPIRequestResult(string fileToParse)
        {
            var reviews = JsonSerializer.Deserialize<APIRequestResult>(fileToParse, serializerOptions);

            if (reviews != null) { return reviews; }
            return new APIRequestResult();
        }

        static public string ParseAPIRequestResult(APIRequestResult fileToParse)
        {
            var reviews = JsonSerializer.Serialize<APIRequestResult>(fileToParse, serializerOptions);

            if (reviews != null) { return reviews; }
            return "";
        }

        static public ReviewSimplified ParseSimplifiedReview(Review review)
        {
            ReviewSimplified temp = new ReviewSimplified();

            temp.authorID = review.author.steamid;
            temp.language = review.language;
            temp.type = review.voted_up ? "Positive" : "Negative";

            temp.review = Formatter.ReviewText(review.review);

            temp.playtime_total = Formatter.Duration(review.author.playtime_forever);
            temp.playtime_last_two_weeks = Formatter.Duration(review.author.playtime_last_two_weeks);
            temp.playtime_at_review = Formatter.Duration(review.author.playtime_at_review);

            temp.review_creation_timestamp = Formatter.Date(review.timestamp_created);
            temp.review_update_timestamp = Formatter.Date(review.timestamp_updated);

            if (review.steam_purchase == false) { temp.purchase_type = PurchaseType.NonSteam; }
            else if (review.received_for_free == true) { temp.purchase_type = PurchaseType.Free; }
            else { temp.purchase_type = PurchaseType.Paid; }

            return temp;
        }
    }
}