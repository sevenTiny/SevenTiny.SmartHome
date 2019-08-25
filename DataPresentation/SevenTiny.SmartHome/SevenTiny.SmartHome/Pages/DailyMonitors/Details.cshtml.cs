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
    public class DetailsModel : PageModel
    {
        private readonly SevenTiny.SmartHome.Models.SmartHomeContext _context;

        public DetailsModel(SevenTiny.SmartHome.Models.SmartHomeContext context)
        {
            _context = context;
        }

        public DailyMonitor DailyMonitor { get; set; }

        public async Task<IActionResult> OnGetAsync(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            DailyMonitor = await _context.DailyMonitor.FirstOrDefaultAsync(m => m.Id == id);

            if (DailyMonitor == null)
            {
                return NotFound();
            }
            return Page();
        }
    }
}
