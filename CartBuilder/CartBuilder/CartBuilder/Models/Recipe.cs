namespace CartBuilder.Models
{
    public class Recipe
    {
        public int Id { get; set; }
        public string ReceipeName { get; set; }
        public string Description { get; set; }
        public int BakeTemperature { get; set; }
        public int BakeTime { get; set; }
        public string Instructions { get; set; }
        public int FoodTypeID { get; set; }
        public int FoodEthnicityID { get; set; }
        public virtual FoodType FoodType { get; set; }
        public virtual FoodEthnicity FoodEthnicity { get; set; }
        public virtual ICollection<Ingredient> Ingredients { get; set; }



    }
}
