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
    public class RecipeIngredientsController : Controller
    {
        private readonly ApplicationDbContext _context;

        public RecipeIngredientsController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: RecipeIngredients
        public async Task<IActionResult> Index()
        {
            var applicationDbContext = _context.RecipeIngredient.Include(r => r.Ingredient);
            return View(await applicationDbContext.ToListAsync());
        }

        // GET: RecipeIngredients/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.RecipeIngredient == null)
            {
                return NotFound();
            }

            var recipeIngredient = await _context.RecipeIngredient
                .Include(r => r.Ingredient)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (recipeIngredient == null)
            {
                return NotFound();
            }

            return View(recipeIngredient);
        }

        // GET: RecipeIngredients/Create
        public IActionResult Create()
        {
            ViewData["IngredientId"] = new SelectList(_context.Ingredient, "Id", "Id");
            return View();
        }

        // POST: RecipeIngredients/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,IngredientId")] RecipeIngredient recipeIngredient)
        {
            if (ModelState.IsValid)
            {
                _context.Add(recipeIngredient);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["IngredientId"] = new SelectList(_context.Ingredient, "Id", "Id", recipeIngredient.IngredientId);
            return View(recipeIngredient);
        }

        // GET: RecipeIngredients/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.RecipeIngredient == null)
            {
                return NotFound();
            }

            var recipeIngredient = await _context.RecipeIngredient.FindAsync(id);
            if (recipeIngredient == null)
            {
                return NotFound();
            }
            ViewData["IngredientId"] = new SelectList(_context.Ingredient, "Id", "Id", recipeIngredient.IngredientId);
            return View(recipeIngredient);
        }

        // POST: RecipeIngredients/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,IngredientId")] RecipeIngredient recipeIngredient)
        {
            if (id != recipeIngredient.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(recipeIngredient);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!RecipeIngredientExists(recipeIngredient.Id))
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
            ViewData["IngredientId"] = new SelectList(_context.Ingredient, "Id", "Id", recipeIngredient.IngredientId);
            return View(recipeIngredient);
        }

        // GET: RecipeIngredients/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.RecipeIngredient == null)
            {
                return NotFound();
            }

            var recipeIngredient = await _context.RecipeIngredient
                .Include(r => r.Ingredient)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (recipeIngredient == null)
            {
                return NotFound();
            }

            return View(recipeIngredient);
        }

        // POST: RecipeIngredients/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.RecipeIngredient == null)
            {
                return Problem("Entity set 'ApplicationDbContext.RecipeIngredient'  is null.");
            }
            var recipeIngredient = await _context.RecipeIngredient.FindAsync(id);
            if (recipeIngredient != null)
            {
                _context.RecipeIngredient.Remove(recipeIngredient);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool RecipeIngredientExists(int id)
        {
          return _context.RecipeIngredient.Any(e => e.Id == id);
        }
    }
}
