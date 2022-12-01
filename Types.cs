// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

namespace Gatherer.Types
{
    public class SteamReviews
    {
        public int success { get; set; }
        public QuerySummary query_summary { get; set; } = new QuerySummary();
        public List<Review> reviews { get; set; } = new List<Review>();
        public string cursor { get; set; } = "*";
    }
    public class QuerySummary
    {
        public int num_reviews { get; set; }
        public int review_score { get; set; }
        public string review_score_desc { get; set; } = "";
        public int total_positive { get; set; }
        public int total_negative { get; set; }
        public int total_reviews { get; set; }
    }
    public class Review
    {
        public string recommendationid { get; set; } = "";
        public Author author { get; set; } = new Author();
        public string language { get; set; } = "";
        public string review { get; set; } = "";
        public int timestamp_created { get; set; }
        public int timestamp_updated { get; set; }
        public bool voted_up { get; set; }
        public int votes_up { get; set; }
        public int votes_funny { get; set; }
        public dynamic weighted_vote_score { get; set; } = "";
        public int comment_count { get; set; }
        public bool steam_purchase { get; set; }
        public bool received_for_free { get; set; }
        public bool written_during_early_access { get; set; }
        public bool hidden_in_steam_china { get; set; }
        public string steam_china_location { get; set; } = "";
    }
    public class Author
    {
        public string steamid { get; set; } = "";
        public int num_games_owned { get; set; }
        public int num_reviews { get; set; }
        public int playtime_forever { get; set; }
        public int playtime_last_two_weeks { get; set; }
        public int playtime_at_review { get; set; }
        public int last_played { get; set; }
    }
    public class ReviewSimplified
    {
        public string authorID { get; set; } = "";                      // The reviewer Steam ID to identify them
        public string playtime_total { get; set; } = "";                // Total playtime as of API Request moment
        public string playtime_last_two_weeks { get; set; } = "";       // Playtime for the last two weeks as of API Request moment
        public string playtime_at_review { get; set; } = "";            // Playtime as of review posted
        public string language { get; set; } = "";                      // Language of the review's author
        public string review { get; set; } = "";                        // Text of the review
        public string review_creation_timestamp { get; set; } = "";     // Timestamp of review creation
        public string review_update_timestamp { get; set; } = "";       // Timestamp of last review update
        public PurchaseType purchase_type { get; set; }                 // Indicates if the player has the game on steam, and if the player has received the game for free
    }
    public enum PurchaseType
    {
        Paid = 0,
        Free = 1,
        NonSteam = 2,
    }
}