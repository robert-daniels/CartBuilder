using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using CartBuilder.Data;
using CartBuilder.Models;

namespace CartBuilder.Controllers
{
    public class FoodEthnicitiesController : Controller
    {
        private readonly ApplicationDbContext _context;

        public FoodEthnicitiesController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: FoodEthnicities
        public async Task<IActionResult> Index()
        {
              return View(await _context.FoodEthnicity.ToListAsync());
        }

        // GET: FoodEthnicities/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.FoodEthnicity == null)
            {
                return NotFound();
            }

            var foodEthnicity = await _context.FoodEthnicity
                .FirstOrDefaultAsync(m => m.Id == id);
            if (foodEthnicity == null)
            {
                return NotFound();
            }

            return View(foodEthnicity);
        }

        // GET: FoodEthnicities/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: FoodEthnicities/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name")] FoodEthnicity foodEthnicity)
        {
            if (ModelState.IsValid)
            {
                _context.Add(foodEthnicity);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(foodEthnicity);
        }

        // GET: FoodEthnicities/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.FoodEthnicity == null)
            {
                return NotFound();
            }

            var foodEthnicity = await _context.FoodEthnicity.FindAsync(id);
            if (foodEthnicity == null)
            {
                return NotFound();
            }
            return View(foodEthnicity);
        }

        // POST: FoodEthnicities/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name")] FoodEthnicity foodEthnicity)
        {
            if (id != foodEthnicity.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(foodEthnicity);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!FoodEthnicityExists(foodEthnicity.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(foodEthnicity);
        }

        // GET: FoodEthnicities/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.FoodEthnicity == null)
            {
                return NotFound();
            }

            var foodEthnicity = await _context.FoodEthnicity
                .FirstOrDefaultAsync(m => m.Id == id);
            if (foodEthnicity == null)
            {
                return NotFound();
            }

            return View(foodEthnicity);
        }

        // POST: FoodEthnicities/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.FoodEthnicity == null)
            {
                return Problem("Entity set 'ApplicationDbContext.FoodEthnicity'  is null.");
            }
            var foodEthnicity = await _context.FoodEthnicity.FindAsync(id);
            if (foodEthnicity != null)
            {
                _context.FoodEthnicity.Remove(foodEthnicity);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool FoodEthnicityExists(int id)
        {
          return _context.FoodEthnicity.Any(e => e.Id == id);
        }
    }
}
