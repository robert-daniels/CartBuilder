namespace CartBuilder.Models
{
    public class RecipeIngredient
    {
        public int Id { get; set; }
        public int IngredientId { get; set; }
        public virtual Recipe Recipe { get; set; }
        public virtual Ingredient Ingredient { get; set; }
    }
}
