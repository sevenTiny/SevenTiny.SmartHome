using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using SevenTiny.SmartHome.Models;

namespace SevenTiny.SmartHome.Pages.DailyMonitors
{
    public class IndexModel : PageModel
    {
        private readonly SevenTiny.SmartHome.Models.SmartHomeContext _context;

        public IndexModel(SevenTiny.SmartHome.Models.SmartHomeContext context)
        {
            _context = context;
        }

        public IList<DailyMonitor> DailyMonitor { get;set; }

        public async Task OnGetAsync()
        {
            DailyMonitor = await _context.DailyMonitor.ToListAsync();
        }
    }
}
