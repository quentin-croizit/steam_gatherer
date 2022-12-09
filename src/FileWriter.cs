// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;

namespace Gatherer
{
    public class FileWriter
    {
        // Private Variables
        static private string reportFileName = "report_";
        static private int[] csvConfigQuoteColumnsIndex = new int[] { 6 };
        static private CsvConfiguration csvConfig = new CsvConfiguration(CultureInfo.InvariantCulture)
        {
            ShouldQuote = args => csvConfigQuoteColumnsIndex.Contains(args.Row.Index),
            Delimiter = ";"
        };

        static public void WriteJSON(string json, string id = "")
        {
            string file_name = reportFileName + id + ".json";  // Formats the name of the output file
            File.WriteAllText(Config.exportFolderPath + file_name, json);
        }

        static public void WriteCSV(List<ReviewSimplified> csv, DateTime request_time)
        {
            string file_name = Config.exportFolderPath + reportFileName + Formatter.Date(request_time) + ".csv";

            using (var writer = new StreamWriter(file_name))
            using (var csvWrtr = new CsvWriter(writer, csvConfig))
            {
                csvWrtr.WriteRecords(csv);
                writer.Flush();
            }
        }
    }
}