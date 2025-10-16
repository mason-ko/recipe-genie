
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';
import 'package:recipe_genie_frontend/models/recipe.dart';
import 'package:recipe_genie_frontend/providers/recipe_provider.dart';
import 'package:recipe_genie_frontend/services/recipe_service.dart';

import 'recipe_provider_test.mocks.dart';

@GenerateMocks([RecipeService])
void main() {
  late RecipeProvider recipeProvider;
  late MockRecipeService mockRecipeService;

  setUp(() {
    mockRecipeService = MockRecipeService();
    recipeProvider = RecipeProvider(recipeService: mockRecipeService);
  });

  group('RecipeProvider', () {
    final recipes = [
      Recipe(id: 1, title: 'Recipe 1'),
      Recipe(id: 2, title: 'Recipe 2'),
    ];

    test('fetchRecipes success', () async {
      when(mockRecipeService.getRecipes()).thenAnswer((_) async => recipes.map((e) => e.toJson()).toList());

      await recipeProvider.fetchRecipes();

      expect(recipeProvider.recipes.length, 2);
      expect(recipeProvider.recipes[0].title, 'Recipe 1');
      expect(recipeProvider.errorMessage, isNull);
      expect(recipeProvider.isLoading, isFalse);
    });

    test('fetchRecipes error', () async {
      when(mockRecipeService.getRecipes()).thenThrow(Exception('Failed to load recipes'));

      await recipeProvider.fetchRecipes();

      expect(recipeProvider.recipes.isEmpty, isTrue);
      expect(recipeProvider.errorMessage, 'Exception: Failed to load recipes');
      expect(recipeProvider.isLoading, isFalse);
    });

    test('generateRecipe success', () async {
      final ingredients = ['ingredient1', 'ingredient2'];
      when(mockRecipeService.generateRecipe(ingredients)).thenAnswer((_) async => {});
      when(mockRecipeService.getRecipes()).thenAnswer((_) async => recipes.map((e) => e.toJson()).toList());

      await recipeProvider.generateRecipe(ingredients);

      expect(recipeProvider.recipes.length, 2);
      expect(recipeProvider.errorMessage, isNull);
      expect(recipeProvider.isLoading, isFalse);
    });

    test('generateRecipe error', () async {
      final ingredients = ['ingredient1', 'ingredient2'];
      when(mockRecipeService.generateRecipe(ingredients)).thenThrow(Exception('Failed to generate recipe'));

      await recipeProvider.generateRecipe(ingredients);

      expect(recipeProvider.recipes.isEmpty, isTrue);
      expect(recipeProvider.errorMessage, 'Exception: Failed to generate recipe');
      expect(recipeProvider.isLoading, isFalse);
    });
  });
}
