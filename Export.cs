// ---------------------------------------------------------------------------- //
// Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) //
// ---------------------------------------------------------------------------- //

using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;
using Gatherer.Types;
using Gatherer.Formatting;

namespace Gatherer.Exporters
{
    public class Export
    {
        static public void JSON(string json, string id = "")
        {
            string file_name = "report_" + id + ".json";                            // Formats the name of the output file
            File.WriteAllText("reports/temp/" + file_name, json);                   // Writes the json to the "reports/temp" folder
        }

        static public void JSON(string json, DateTime request_time)
        {
            string file_name = "report_" + Format.Date(request_time) + ".json";     // Formats the name of the output file
            File.WriteAllText("reports/" + file_name, json);                        // Writes the json to the "reports/" folder
        }

        static public void CSV(List<ReviewSimplified> csv, DateTime request_time)
        {
            int[] indexes = new int[] { 4, 5 };
            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                ShouldQuote = args => indexes.Contains(args.Row.Index),
                Delimiter = ";"
            };

            string file_name = "reports/report_" + Format.Date(request_time) + ".csv";

            using (var writer = new StreamWriter(file_name))
            using (var csvWrtr = new CsvWriter(writer, config))
            {
                csvWrtr.WriteRecords(csv);
                writer.Flush();
            }
        }
    }
}