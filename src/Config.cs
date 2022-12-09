// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using System.Text.RegularExpressions;

namespace Gatherer
{
    public class Config
    {
        // Public Variables
        static public string exportFolderPath = "";

        // Private Variables
        static private string configFile = "";
        static private string exportFolderRegex = @"(?<=Report Folder:(\s*|)\042)([^(\n|\r)])*(?=\042(\n|\r))";

        static public void ReadConfig()
        {
            configFile = File.ReadAllText("config");

            exportFolderPath = GetExportFolder();
        }

        static private string GetExportFolder()
        {
            string folder = Regex.Match(configFile, exportFolderRegex, RegexOptions.Multiline).Value;

            if (!Directory.Exists(folder))
            { Directory.CreateDirectory(folder); }

            return folder;
        }
    }
}