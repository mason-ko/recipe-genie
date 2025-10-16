
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import 'package:recipe_genie_frontend/providers/auth_provider.dart';
import 'package:recipe_genie_frontend/providers/recipe_provider.dart';
import 'package:recipe_genie_frontend/widgets/recipe_card.dart';
import 'package:flutter_typeahead/flutter_typeahead.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final List<String> _ingredients = [];
  final TextEditingController _ingredientController = TextEditingController();

  static const List<String> _commonIngredients = <String>[
    'Chicken', 'Beef', 'Pork', 'Fish', 'Shrimp', 'Tofu', 'Eggs', 'Milk', 'Cheese', 'Butter', 'Flour', 'Sugar', 'Salt', 'Pepper', 'Olive oil', 'Onion', 'Garlic', 'Tomatoes', 'Potatoes', 'Carrots', 'Broccoli', 'Spinach', 'Lettuce', 'Rice', 'Pasta', 'Bread'
  ];

  @override
  void initState() {
    super.initState();
    // Fetch recipes when the screen is initialized
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<RecipeProvider>(context, listen: false).fetchRecipes();
    });
  }

  void _addIngredient(String ingredient) {
    if (ingredient.isNotEmpty) {
      setState(() {
        _ingredients.add(ingredient);
        _ingredientController.clear();
      });
    }
  }

  void _removeIngredient(int index) {
    setState(() {
      _ingredients.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);
    final user = authProvider.user;

    return Scaffold(
      appBar: AppBar(
        title: Text(user?.name ?? 'Recipe Genie'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              authProvider.logout();
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TypeAheadField(
              controller: _ingredientController,
              suggestionsCallback: (pattern) {
                return _commonIngredients.where((item) => item.toLowerCase().contains(pattern.toLowerCase())).toList();
              },
              itemBuilder: (context, suggestion) {
                return ListTile(
                  title: Text(suggestion),
                );
              },
              onSelected: (suggestion) {
                _addIngredient(suggestion);
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Wrap(
              spacing: 8.0,
              children: _commonIngredients.take(5).map((ingredient) {
                return ActionChip(
                  label: Text(ingredient),
                  onPressed: () {
                    _addIngredient(ingredient);
                  },
                );
              }).toList(),
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _ingredients.length,
              itemBuilder: (context, index) {
                final ingredient = _ingredients[index];
                return ListTile(
                  title: Text(ingredient),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () => _removeIngredient(index),
                  ),
                );
              },
            ),
          ),
          const Divider(),
          Expanded(
            flex: 2,
            child: Consumer<RecipeProvider>(
              builder: (context, recipeProvider, child) {
                if (recipeProvider.errorMessage != null) {
                  WidgetsBinding.instance.addPostFrameCallback((_) {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text(recipeProvider.errorMessage!),
                      ),
                    );
                  });
                }

                if (recipeProvider.isLoading) {
                  return const Center(child: CircularProgressIndicator());
                }

                if (recipeProvider.recipes.isEmpty) {
                  return const Center(child: Text('No recipes found.'));
                }

                return ListView.builder(
                  itemCount: recipeProvider.recipes.length,
                  itemBuilder: (context, index) {
                    final recipe = recipeProvider.recipes[index];
                    return RecipeCard(recipe: recipe);
                  },
                );
              },
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Provider.of<RecipeProvider>(context, listen: false)
              .generateRecipe(_ingredients);
        },
        child: const Icon(Icons.restaurant_menu),
      ),
    );
  }
}
