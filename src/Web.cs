// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Web;

namespace Gatherer
{
    public class Web
    {
        // Instances
        static private HttpClient client = new HttpClient();
        static private Random random = new Random();

        // Private Variables
        static private string baseRequestURL = "https://store.steampowered.com/appreviews/";

        static public string CreateURL(List<string> arguments)
        {
            baseRequestURL += arguments[0];                                    // Puts the App ID in the request
            baseRequestURL += "?json=1";                                       // Adds the json parameter
            baseRequestURL += "&filter=" + arguments[1];                       // Adds the filter argument
            baseRequestURL += "&language=" + arguments[2];                     // Adds the language argument
            baseRequestURL += "&day_range=" + arguments[3];                    // Adds the day range argument
            baseRequestURL += "&review_type=" + arguments[4];                  // Adds review type argument
            baseRequestURL += "&purchase_type=" + arguments[5];                // Adds purchase type argument
            baseRequestURL += "&num_per_page=";                                // Adds num per page argument

            return baseRequestURL;
        }

        static public APIRequestResult MakeWebRequest(string requestURL, int requestReviewNumber, string requestCursor)
        {
            string tempFinalURL = requestURL + requestReviewNumber + "&cursor=" + Encode(requestCursor);
            string requestResult = client.GetAsync(tempFinalURL).Result.Content.ReadAsStringAsync().Result;

            return Parser.ParseAPIRequestResult(requestResult);
        }

        static private string Encode(string textToEncode)
        {
            return HttpUtility.UrlEncode(textToEncode);
        }
    }
}