
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import 'package:recipe_genie_frontend/models/recipe.dart';
import 'package:recipe_genie_frontend/providers/auth_provider.dart';

import 'package:recipe_genie_frontend/screens/home_screen.dart';
import 'package:recipe_genie_frontend/screens/login_screen.dart';
import 'package:recipe_genie_frontend/screens/recipe_detail_screen.dart';

GoRouter createRouter(AuthProvider authProvider) {
  return GoRouter(
    refreshListenable: authProvider,
    initialLocation: '/',
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const LoginScreen(),
      ),
      GoRoute(
        path: '/home',
        builder: (context, state) => const HomeScreen(),
        routes: [
          GoRoute(
            path: 'recipe',
            builder: (context, state) {
              final recipe = state.extra as Recipe;
              return RecipeDetailScreen(recipe: recipe);
            },
          ),
        ],
      ),
    ],
  );
}
