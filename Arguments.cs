// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.RegularExpressions;
using Gatherer.Arguments.Presets;

namespace Gatherer.Arguments
{
    public class Args
    {
        static List<string> args_keywords = new List<string> { "id=", "filter=", "lang=", "range=", "type=", "purchase=", "number=" };
        static List<string> args_list = new List<string>(7);
        static List<string> args_regex = new List<string> { "[0-9]+",
                                                            "(all|recent|updated)",
                                                            "[a-z]+",
                                                            "([0-9]{1,3}|all)",
                                                            "(all|positive|negative)",
                                                            "(all|non_steam_purchase|steam)",
                                                            "[0-9]+" };
        static string request_url = "https://store.steampowered.com/appreviews/";

        static public List<string> DecodeCLIArguments(List<string> arguments)
        {
            args_list = Preset.CheckForPreset(arguments);
            args_list = OrganizeArguments(args_list, arguments);

            foreach (string arg in args_list)
            {
                Console.WriteLine("Entered Arguments : " + arg);
            }
            return args_list;
        }

        static public string CreateURL(List<string> arguments)
        {
            request_url += arguments[0];                                    // Puts the App ID in the request
            request_url += "?json=1";                                       // Adds the json parameter
            request_url += "&filter=" + arguments[1];                       // Adds the filter argument
            request_url += "&language=" + arguments[2];                     // Adds the language argument
            request_url += "&day_range=" + arguments[3];                    // Adds the day range argument
            request_url += "&review_type=" + arguments[4];                  // Adds review type argument
            request_url += "&purchase_type=" + arguments[5];                // Adds purchase type argument
            request_url += "&num_per_page=";                                // Adds num per page argument

            return request_url;
        }

        static private List<string> OrganizeArguments(List<string> final_list, List<string> original_arguments)
        {
            for (int i = 0; i < 7; i++)
            {
                string temp = args_keywords[i] + args_regex[i];
                foreach (string arg in original_arguments)
                {
                    if (Regex.Match(arg, temp).Success)
                    {
                        Console.WriteLine(arg);
                        final_list[i] = Regex.Replace(arg, @"[a-z]+=", String.Empty);
                    }
                }
            }
            return final_list;
        }
    }
}