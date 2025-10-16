
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';
import 'package:recipe_genie_frontend/providers/recipe_provider.dart';
import 'package:recipe_genie_frontend/screens/home_screen.dart';
import 'package:recipe_genie_frontend/core/router.dart';

import 'package:recipe_genie_frontend/core/theme.dart';

import 'package:recipe_genie_frontend/providers/auth_provider.dart';

Future<void> main() async {
  await dotenv.load();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => AuthProvider()),
        ChangeNotifierProvider(create: (context) => RecipeProvider()),
      ],
      child: Builder(
        builder: (context) {
          final authProvider = Provider.of<AuthProvider>(context);
          return MaterialApp.router(
            title: 'Recipe Genie',
            theme: appTheme,
            routerConfig: createRouter(authProvider),
          );
        },
      ),
    );
  }
}

