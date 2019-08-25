using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace SevenTiny.SmartHome.Models
{
    public partial class DailyMonitor
    {
        [Key]
        public int Id { get; set; }
        public DateTime DateTime { get; set; }
        public int? Year { get; set; }
        public int? Month { get; set; }
        public int? Day { get; set; }
        public int? Hour { get; set; }
        public double? Temperature { get; set; }
        public double? Humidity { get; set; }
    }
}
