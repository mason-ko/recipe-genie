
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';
import 'package:provider/provider.dart';
import 'package:recipe_genie_frontend/models/recipe.dart';
import 'package:recipe_genie_frontend/providers/recipe_provider.dart';
import 'package:recipe_genie_frontend/screens/home_screen.dart';

import 'home_screen_test.mocks.dart';

@GenerateMocks([RecipeProvider])
void main() {
  late MockRecipeProvider mockRecipeProvider;

  setUp(() {
    mockRecipeProvider = MockRecipeProvider();
  });

  Widget createHomeScreen() => ChangeNotifierProvider<RecipeProvider>.value(
        value: mockRecipeProvider,
        child: MaterialApp(
          home: const HomeScreen(),
          scaffoldMessengerKey: GlobalKey<ScaffoldMessengerState>(),
        ),
      );

  group('HomeScreen', () {
    testWidgets('shows loading indicator when loading', (tester) async {
      when(mockRecipeProvider.isLoading).thenReturn(true);
      when(mockRecipeProvider.recipes).thenReturn([]);
      when(mockRecipeProvider.errorMessage).thenReturn(null);

      await tester.pumpWidget(createHomeScreen());

      expect(find.byType(CircularProgressIndicator), findsOneWidget);
    });

    testWidgets('shows list of recipes when loaded', (tester) async {
      final recipes = [Recipe(id: 1, title: 'Recipe 1')];
      when(mockRecipeProvider.isLoading).thenReturn(false);
      when(mockRecipeProvider.recipes).thenReturn(recipes);
      when(mockRecipeProvider.errorMessage).thenReturn(null);

      await tester.pumpWidget(createHomeScreen());

      expect(find.text('Recipe 1'), findsOneWidget);
    });

    testWidgets('shows error message when error occurs', (tester) async {
      when(mockRecipeProvider.isLoading).thenReturn(false);
      when(mockRecipeProvider.recipes).thenReturn([]);
      when(mockRecipeProvider.errorMessage).thenReturn('Error');

      await tester.pumpWidget(createHomeScreen());
      await tester.pumpAndSettle();

      expect(find.byType(SnackBar), findsOneWidget);
      expect(find.text('Error'), findsOneWidget);
    });
  });
}
