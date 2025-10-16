
import 'package:flutter/material.dart';
import 'package:recipe_genie_frontend/models/recipe.dart';
import 'package:recipe_genie_frontend/services/recipe_service.dart';

class RecipeProvider with ChangeNotifier {
  late final RecipeService _recipeService;
  List<Recipe> _recipes = [];
  bool _isLoading = false;
  String? _errorMessage;

  RecipeProvider({RecipeService? recipeService}) {
    _recipeService = recipeService ?? RecipeService();
  }

  List<Recipe> get recipes => _recipes;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> fetchRecipes() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      final List<dynamic> recipeData = await _recipeService.getRecipes();
      _recipes = recipeData.map((data) => Recipe.fromJson(data)).toList();
    } catch (e) {
      _errorMessage = e.toString();
    }
    _isLoading = false;
    notifyListeners();
  }

  Future<void> generateRecipe(List<String> ingredients) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      await _recipeService.generateRecipe(ingredients);
      await fetchRecipes();
    } catch (e) {
      _errorMessage = e.toString();
    }
    _isLoading = false;
    notifyListeners();
  }
}
