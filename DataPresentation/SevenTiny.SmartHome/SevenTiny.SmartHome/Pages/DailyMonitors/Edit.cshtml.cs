using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using SevenTiny.SmartHome.Models;

namespace SevenTiny.SmartHome.Pages.DailyMonitors
{
    public class EditModel : PageModel
    {
        private readonly SevenTiny.SmartHome.Models.SmartHomeContext _context;

        public EditModel(SevenTiny.SmartHome.Models.SmartHomeContext context)
        {
            _context = context;
        }

        [BindProperty]
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

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.Attach(DailyMonitor).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!DailyMonitorExists(DailyMonitor.Id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return RedirectToPage("./Index");
        }

        private bool DailyMonitorExists(int id)
        {
            return _context.DailyMonitor.Any(e => e.Id == id);
        }
    }
}
