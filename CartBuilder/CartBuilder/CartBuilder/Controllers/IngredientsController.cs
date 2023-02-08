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
    public class IngredientsController : Controller
    {
        private readonly ApplicationDbContext _context;

        public IngredientsController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: Ingredients
        public async Task<IActionResult> Index()
        {
            var applicationDbContext = _context.Ingredient.Include(i => i.UnitOfMeasure);
            return View(await applicationDbContext.ToListAsync());
        }

        // GET: Ingredients/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.Ingredient == null)
            {
                return NotFound();
            }

            var ingredient = await _context.Ingredient
                .Include(i => i.UnitOfMeasure)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (ingredient == null)
            {
                return NotFound();
            }

            return View(ingredient);
        }

        // GET: Ingredients/Create
        public IActionResult Create()
        {
            ViewData["UnitOfMeasureId"] = new SelectList(_context.Set<UnitOfMeasure>(), "Id", "Name");
            return View();
        }

        // POST: Ingredients/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,Amount,UnitOfMeasureId")] Ingredient ingredient)
        {
            if (ModelState.IsValid)
            {
                _context.Add(ingredient);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["UnitOfMeasureId"] = new SelectList(_context.Set<UnitOfMeasure>(), "Id", "Name", ingredient.UnitOfMeasureId);
            return View(ingredient);
        }

        // GET: Ingredients/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.Ingredient == null)
            {
                return NotFound();
            }

            var ingredient = await _context.Ingredient.FindAsync(id);
            if (ingredient == null)
            {
                return NotFound();
            }
            ViewData["UnitOfMeasureId"] = new SelectList(_context.Set<UnitOfMeasure>(), "Id", "Id", ingredient.UnitOfMeasureId);
            return View(ingredient);
        }

        // POST: Ingredients/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Amount,UnitOfMeasureId")] Ingredient ingredient)
        {
            if (id != ingredient.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(ingredient);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!IngredientExists(ingredient.Id))
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
            ViewData["UnitOfMeasureId"] = new SelectList(_context.Set<UnitOfMeasure>(), "Id", "Id", ingredient.UnitOfMeasureId);
            return View(ingredient);
        }

        // GET: Ingredients/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.Ingredient == null)
            {
                return NotFound();
            }

            var ingredient = await _context.Ingredient
                .Include(i => i.UnitOfMeasure)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (ingredient == null)
            {
                return NotFound();
            }

            return View(ingredient);
        }

        // POST: Ingredients/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.Ingredient == null)
            {
                return Problem("Entity set 'ApplicationDbContext.Ingredient'  is null.");
            }
            var ingredient = await _context.Ingredient.FindAsync(id);
            if (ingredient != null)
            {
                _context.Ingredient.Remove(ingredient);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool IngredientExists(int id)
        {
          return _context.Ingredient.Any(e => e.Id == id);
        }
    }
}
