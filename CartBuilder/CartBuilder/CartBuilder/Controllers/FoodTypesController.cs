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
    public class FoodTypesController : Controller
    {
        private readonly ApplicationDbContext _context;

        public FoodTypesController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: FoodTypes
        public async Task<IActionResult> Index()
        {
              return View(await _context.FoodType.ToListAsync());
        }

        // GET: FoodTypes/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.FoodType == null)
            {
                return NotFound();
            }

            var foodType = await _context.FoodType
                .FirstOrDefaultAsync(m => m.Id == id);
            if (foodType == null)
            {
                return NotFound();
            }

            return View(foodType);
        }

        // GET: FoodTypes/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: FoodTypes/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name")] FoodType foodType)
        {
            if (ModelState.IsValid)
            {
                _context.Add(foodType);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(foodType);
        }

        // GET: FoodTypes/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.FoodType == null)
            {
                return NotFound();
            }

            var foodType = await _context.FoodType.FindAsync(id);
            if (foodType == null)
            {
                return NotFound();
            }
            return View(foodType);
        }

        // POST: FoodTypes/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name")] FoodType foodType)
        {
            if (id != foodType.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(foodType);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!FoodTypeExists(foodType.Id))
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
            return View(foodType);
        }

        // GET: FoodTypes/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.FoodType == null)
            {
                return NotFound();
            }

            var foodType = await _context.FoodType
                .FirstOrDefaultAsync(m => m.Id == id);
            if (foodType == null)
            {
                return NotFound();
            }

            return View(foodType);
        }

        // POST: FoodTypes/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.FoodType == null)
            {
                return Problem("Entity set 'ApplicationDbContext.FoodType'  is null.");
            }
            var foodType = await _context.FoodType.FindAsync(id);
            if (foodType != null)
            {
                _context.FoodType.Remove(foodType);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool FoodTypeExists(int id)
        {
          return _context.FoodType.Any(e => e.Id == id);
        }
    }
}
