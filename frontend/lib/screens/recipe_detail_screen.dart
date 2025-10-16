
import 'package:flutter/material.dart';
import 'package:recipe_genie_frontend/models/recipe.dart';

class RecipeDetailScreen extends StatelessWidget {
  final Recipe recipe;

  const RecipeDetailScreen({super.key, required this.recipe});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(recipe.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (recipe.description != null)
              Text(
                recipe.description!,
                style: const TextStyle(fontSize: 16.0),
              ),
            const SizedBox(height: 16.0),
            const Text(
              'Instructions',
              style: TextStyle(
                fontSize: 20.0,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8.0),
            if (recipe.instructions != null)
              Text(
                recipe.instructions!,
                style: const TextStyle(fontSize: 16.0),
              ),
          ],
        ),
      ),
    );
  }
}
