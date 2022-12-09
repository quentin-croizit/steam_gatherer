// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.RegularExpressions;

namespace Gatherer
{
    public class Formatter
    {
        static public string Duration(int duration) // Formats duration to the XXhXXm format given an integer representating the number of minutes
        {
            return string.Format("{0:000}h{1:00}m", TimeSpan.FromMinutes(duration).TotalHours, duration % 60);
        }

        static public string ReviewText(string reviewText) // Formats review text by removing new lines and adding " | " to replace them
        {
            return Regex.Replace(reviewText.Trim(), @"$(\r|\n)*(?=[\s\S])", " | ", RegexOptions.Multiline);
        }

        static public string Date(DateTime date) // Formats a date to the XX-XX-XXXX format given a DateTime
        {
            return date.ToString().Replace(":", "-").Replace("/", "-").Replace(" ", "_");
        }

        static public string Date(int unixTime) // Formats a date to the XX-XX-XXXX format given an integer representating a unix time
        {
            return Regex.Replace(DateTimeOffset.FromUnixTimeSeconds(unixTime).ToString(), @"(\+([0-9]+(:|))+)|(:[0-9]{2}\s)", String.Empty);
        }
    }
}