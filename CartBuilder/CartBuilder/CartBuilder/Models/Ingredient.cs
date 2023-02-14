namespace CartBuilder.Models
{
    public class Ingredient
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public double Amount { get; set; }
        public int? UnitOfMeasureId { get; set; }
        public virtual UnitOfMeasure UnitOfMeasure { get; set; }
        public virtual ICollection<RecipeIngredient> IngredientRecipes
        { get; set; }
    }

}
