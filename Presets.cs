// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

namespace Gatherer.Arguments.Presets
{
    public class Preset
    {
        static public List<string> CheckForPreset(List<string> cli_arguments)
        {
            List<string> arguments = new List<string>();

            if (cli_arguments.Count == 0) { cli_arguments.Add("default"); }     // If no arguments are given  and no preset is selected then default is given

            switch (cli_arguments[0].ToString())
            {
                case "default":
                    arguments = default_args;
                    Console.WriteLine("Default Preset selected");
                    break;

                case "test":
                    arguments = test_args;
                    Console.WriteLine("Test Preset selected");
                    break;

                default:
                    arguments = default_args;
                    Console.WriteLine("No Preset was found.");
                    break;
            }

            return arguments;
        }

        static List<string> default_args = new List<string> { "1245620", "all", "english", "5", "all", "all", "20" };
        static List<string> test_args = new List<string> { "1245620", "recent", "english", "1", "positive", "steam", "1" };
    }
}