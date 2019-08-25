using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using SevenTiny.SmartHome.Models;

namespace SevenTiny.SmartHome.Pages.DailyMonitors
{
    public class CreateModel : PageModel
    {
        private readonly SevenTiny.SmartHome.Models.SmartHomeContext _context;

        public CreateModel(SevenTiny.SmartHome.Models.SmartHomeContext context)
        {
            _context = context;
        }

        public IActionResult OnGet()
        {
            return Page();
        }

        [BindProperty]
        public DailyMonitor DailyMonitor { get; set; }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.DailyMonitor.Add(DailyMonitor);
            await _context.SaveChangesAsync();

            return RedirectToPage("./Index");
        }
    }
}