// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

namespace Gatherer
{
    public class APIRequestResult
    {
        public int success { get; set; }                                        // 1 : Query was successful
        public QuerySummary query_summary { get; set; } = new QuerySummary();   // Summary of the query made to api
        public List<Review> reviews { get; set; } = new List<Review>();         // List of the reviews returned in the query 
        public string cursor { get; set; } = "*";                               // Value used to get the next query from the api
    }
    public class QuerySummary
    {
        public int num_reviews { get; set; }                                    // Number of reviews included in the query
        public int review_score { get; set; }                                   // Score of the reviews
        public string review_score_desc { get; set; } = "";                     // Description of reviews score 
        public int total_positive { get; set; }                                 // Total number of positive reviews of the game
        public int total_negative { get; set; }                                 // Total number of negative reviews of the game
        public int total_reviews { get; set; }                                  // Total number of reviews of the game
    }
    public class Review
    {
        public string recommendationid { get; set; } = "";                      // ID of the review
        public Author author { get; set; } = new Author();                      // Information about the review's author
        public string language { get; set; } = "";                              // Language of the review
        public string review { get; set; } = "";                                // Text of the review
        public int timestamp_created { get; set; }                              // Time of creation of the review (unix time)
        public int timestamp_updated { get; set; }                              // Time of last update of the review (unix time)
        public bool voted_up { get; set; }                                      // False:Negative | True:Positive
        public int votes_up { get; set; }                                       // Number of votes up of the review
        public int votes_funny { get; set; }                                    // Number of votes funny of the review
        public dynamic weighted_vote_score { get; set; } = "";                  // Helpfulness Score
        public int comment_count { get; set; }                                  // Number of comments posted on the review
        public bool steam_purchase { get; set; }                                // False : Non-Steam Game | True : Steam Game
        public bool received_for_free { get; set; }                             // True : Game was received for free
        public bool written_during_early_access { get; set; }                   // True : Review was written during early access
        public bool hidden_in_steam_china { get; set; }                         // True : Review is hidden in china
        public string steam_china_location { get; set; } = "";                  // No Idea how it is formatted
        public string developer_response { get; set; } = "";                    // Developer response if any
        public int timestamp_dev_responded { get; set; }                        // Developer response timestamp (unix time)

    }
    public class Author
    {
        public string steamid { get; set; } = "";                               // Author's Steam ID
        public int num_games_owned { get; set; }                                // Number of games owned by the author
        public int num_reviews { get; set; }                                    // Number of reviews made by the author
        public int playtime_forever { get; set; }                               // Total playtime of the game by the author at query time 
        public int playtime_last_two_weeks { get; set; }                        // Playtime of the game for the last 2 weeks by the author at query time 
        public int playtime_at_review { get; set; }                             // Total playtime of the game by the author at review time 
        public int last_played { get; set; }                                    // Last time the author played the game
    }
    public class ReviewSimplified
    {
        public string authorID { get; set; } = "";                              // The reviewer Steam ID to identify them
        public string playtime_total { get; set; } = "";                        // Total playtime as of API Request moment
        public string playtime_last_two_weeks { get; set; } = "";               // Playtime for the last two weeks as of API Request moment
        public string playtime_at_review { get; set; } = "";                    // Playtime as of review posted
        public string language { get; set; } = "";                              // Language of the review's author
        public string type { get; set; } = "";                                  // Type of the review
        public string review { get; set; } = "";                                // Text of the review
        public string review_creation_timestamp { get; set; } = "";             // Timestamp of review creation
        public string review_update_timestamp { get; set; } = "";               // Timestamp of last review update
        public PurchaseType purchase_type { get; set; }                         // Indicates if the player has the game on steam, and if the player has received the game for free
    }
    public enum PurchaseType
    {
        Paid = 0,
        Free = 1,
        NonSteam = 2,
    }
}