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
    public class UnitOfMeasuresController : Controller
    {
        private readonly ApplicationDbContext _context;

        public UnitOfMeasuresController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: UnitOfMeasures
        public async Task<IActionResult> Index()
        {
              return View(await _context.UnitOfMeasure.ToListAsync());
        }

        // GET: UnitOfMeasures/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.UnitOfMeasure == null)
            {
                return NotFound();
            }

            var unitOfMeasure = await _context.UnitOfMeasure
                .FirstOrDefaultAsync(m => m.Id == id);
            if (unitOfMeasure == null)
            {
                return NotFound();
            }

            return View(unitOfMeasure);
        }

        // GET: UnitOfMeasures/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: UnitOfMeasures/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name")] UnitOfMeasure unitOfMeasure)
        {
            if (ModelState.IsValid)
            {
                _context.Add(unitOfMeasure);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(unitOfMeasure);
        }

        // GET: UnitOfMeasures/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.UnitOfMeasure == null)
            {
                return NotFound();
            }

            var unitOfMeasure = await _context.UnitOfMeasure.FindAsync(id);
            if (unitOfMeasure == null)
            {
                return NotFound();
            }
            return View(unitOfMeasure);
        }

        // POST: UnitOfMeasures/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name")] UnitOfMeasure unitOfMeasure)
        {
            if (id != unitOfMeasure.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(unitOfMeasure);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!UnitOfMeasureExists(unitOfMeasure.Id))
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
            return View(unitOfMeasure);
        }

        // GET: UnitOfMeasures/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.UnitOfMeasure == null)
            {
                return NotFound();
            }

            var unitOfMeasure = await _context.UnitOfMeasure
                .FirstOrDefaultAsync(m => m.Id == id);
            if (unitOfMeasure == null)
            {
                return NotFound();
            }

            return View(unitOfMeasure);
        }

        // POST: UnitOfMeasures/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.UnitOfMeasure == null)
            {
                return Problem("Entity set 'ApplicationDbContext.UnitOfMeasure'  is null.");
            }
            var unitOfMeasure = await _context.UnitOfMeasure.FindAsync(id);
            if (unitOfMeasure != null)
            {
                _context.UnitOfMeasure.Remove(unitOfMeasure);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool UnitOfMeasureExists(int id)
        {
          return _context.UnitOfMeasure.Any(e => e.Id == id);
        }
    }
}
