// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using Gatherer.Arguments;
using Gatherer.Types;
using Gatherer.Exporters;
using Gatherer.WebRequest;
using Gatherer.JsonManager;

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
        //          App ID ··········· 7-digit number used to identify a game                                                                                       //
        //          Argument prefix : id=                                                                                                                           //
        //                                                                                                                                                          //
        //          Filter ··········· all | recent | updated ; used to filter gathered reviews by the most recents, the last updated, or by relevance (all)        //
        //          Argument prefix : filter=                                                                                                                       //
        //                                                                                                                                                          //
        //          Language ········· Lang code used to used to filter gathered reviews by languages, codes can be found on the Steam API Doc                      //
        //          Argument prefix : lang=                                                                                                                         //
        //                                                                                                                                                          //
        //          Day Range ········ Number ranging from 0-365 ; only reviews sent from today - day range will be gathered (only works with filter:all)           //
        //          Argument prefix : range=                                                                                                                        //
        //                                                                                                                                                          //
        //          Review Type ······ all | positive | negative ; used to filter gathered reviews by the type of review                                            //
        //          Argument prefix : type=                                                                                                                         //
        //                                                                                                                                                          //
        //          Purchase Type ···· all | non_steam_purchase | steam ; used to filter gathered reviews by where it was purchased                                 //
        //          Argument prefix : purchase=                                                                                                                     //
        //                                                                                                                                                          //
        //          Num per Page ····· Number ranging from 1-100 ; Number of reviews sent in every request                                                          //
        //          Argument prefix : number=                                                                                                                       //
        //                                                                                                                                                          //
        //                                                                                                                                                          //
        //        **Arguments Presets**                                                                                                                             //
        //          You can also use presets which contains predetermined arguments. To use them just indicate their name without any                               //
        //          prefix before their name.                                                                                                                       //
        //                                                                                                                                                          //
        //          Those presets can also be modified, so if you want to use a preset but only change the lang of it, use the name of the                          //
        //          preset and add the "lang=" prefeix followed by the lang you want.                                                                               //
        //                                                                                                                                                          //
        // -------------------------------------------------------------------------------------------------------------------------------------------------------- //
        //                                                                                                                                                          //
        //        CLI Exemple Arguments :                                                                                                                           //
        //          dotnet run                                                                                                                           //
        //          dotnet run -- default                                                                                                                           //
        //          dotnet run -- lang=english filter=recent                                                                                                                           //
        //          dotnet run -- default id=12345 number=150                                                                                                                           //
        //          dotnet run -- range=31 type=positive test                                                                                                                           //
        //                                                                                                                                                          //
        // -------------------------------------------------------------------------------------------------------------------------------------------------------- //

        static List<string> arguments = new List<string>(7);
        static string request_url = "";
        static DateTime request_time;
        static SteamReviews data = new SteamReviews();
        static List<ReviewSimplified> csv = new List<ReviewSimplified>();

        static void Main(string[] args)
        {
            arguments = Args.DecodeCLIArguments(args.ToList());
            request_url = Args.CreateURL(arguments);

            request_time = DateTime.Now;

            Request.GetJSON(request_url, Int16.Parse(arguments[6]));
            data = Json.combineJSON(request_time);
            csv = Json.json2csv(data);
            Export.CSV(csv, request_time);
        }
    }
}