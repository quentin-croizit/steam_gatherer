// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Web;
using Gatherer.Exporters;
using Gatherer.JsonManager;

namespace Gatherer.WebRequest
{
    public class Request
    {
        static int id = 0;
        static string request = "";
        static string cursor = "*";
        static HttpClient client = new HttpClient();
        static HttpResponseMessage request_result = new HttpResponseMessage();
        static Random rnd = new Random();

        static public void GetJSON(string request_url, int review_number_arg)
        {
            while (review_number_arg > 100)
            {
                int num = rnd.Next(80, 100);
                makeRequest(request_url, review_number_arg, cursor);

                review_number_arg -= num;
                id++;

                RequestDelay();
            }

            makeRequest(request_url, review_number_arg, cursor);
            review_number_arg = 0;
        }

        static private void makeRequest(string request_url, int num_per_page, string cursor)
        {
            request_result = client.GetAsync(request_url + num_per_page + "&cursor=" + Encode(cursor)).Result;
            request = request_result.Content.ReadAsStringAsync().Result;

            Export.JSON(request, id.ToString());
            cursor = Json.parseJSON(request).cursor;
        }

        static private string Encode(string textToEncode)
        {
            return HttpUtility.UrlEncode(textToEncode);
        }

        static private void RequestDelay()
        {
            int num = rnd.Next(2, 5);
            Thread.Sleep(num * 50);
        }
    }
}