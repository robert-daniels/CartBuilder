using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using CartBuilder.Models;

namespace CartBuilder.Data
{
    public class ApplicationDbContext : IdentityDbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
        public DbSet<CartBuilder.Models.FoodEthnicity> FoodEthnicity { get; set; }
        public DbSet<CartBuilder.Models.FoodType> FoodType { get; set; }
        public DbSet<CartBuilder.Models.Ingredient> Ingredient { get; set; }
        public DbSet<CartBuilder.Models.Recipe> Recipe { get; set; }
        public DbSet<CartBuilder.Models.RecipeIngredient> RecipeIngredient { get; set; }
        public DbSet<CartBuilder.Models.UnitOfMeasure> UnitOfMeasure { get; set; }
    }
}