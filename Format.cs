// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.RegularExpressions;

namespace Gatherer.Formatting
{
    public class Format
    {
        static public string Duration(int time)
        {
            string tempStr = "";
            double tempInt = Math.Floor(time / 60f);

            tempStr += tempInt.ToString() + "h";

            tempInt *= 60;
            tempInt = time - tempInt;

            tempStr += tempInt.ToString() + "m";

            return tempStr;
        }

        static public string Text(string reviewText)
        {
            string temp = "";

            temp = Regex.Replace(reviewText, @"^$[\r|\n]*", String.Empty, RegexOptions.Multiline);
            temp = temp.Trim();
            temp = Regex.Replace(temp, @"\n|\r", " | ", RegexOptions.Multiline);

            return temp;
        }

        static public string Date(DateTime date)
        {
            return date.ToString().Replace(":", "-").Replace("/", "-").Replace(" ", "_");
        }

        static public string Date(int unixTime)
        {
            string temp = "";

            temp = DateTimeOffset.FromUnixTimeSeconds(unixTime).ToString();

            temp = Regex.Replace(temp, @"\+([0-9]+(:|))+", String.Empty);
            temp = Regex.Replace(temp, @":[0-9]{2}\s", String.Empty);

            return temp;
        }
    }
}