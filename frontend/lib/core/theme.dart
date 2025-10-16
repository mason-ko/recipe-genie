
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

const Color primaryColor = Color(0xFFC0A063);
const Color secondaryColor = Color(0xFF2C2C2C);
const Color backgroundColor = Color(0xFFF5F5F5);
const Color textColor = Color(0xFF333333);

final ThemeData appTheme = ThemeData(
  primaryColor: primaryColor,
  colorScheme: const ColorScheme.light(
    primary: primaryColor,
    secondary: secondaryColor,
    background: backgroundColor,
    onBackground: textColor,
  ),
  scaffoldBackgroundColor: backgroundColor,
  textTheme: GoogleFonts.playfairDisplayScTextTheme(
    const TextTheme(
      displayLarge: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      displayMedium: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      displaySmall: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      headlineLarge: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      headlineMedium: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      headlineSmall: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      titleLarge: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      titleMedium: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      titleSmall: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      bodyLarge: TextStyle(color: textColor),
      bodyMedium: TextStyle(color: textColor),
      bodySmall: TextStyle(color: textColor),
      labelLarge: TextStyle(color: textColor, fontWeight: FontWeight.bold),
      labelMedium: TextStyle(color: textColor),
      labelSmall: TextStyle(color: textColor),
    ),
  ),
  appBarTheme: const AppBarTheme(
    backgroundColor: secondaryColor,
    foregroundColor: Colors.white,
    elevation: 0,
  ),
  cardTheme: CardThemeData(
    elevation: 2,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
  floatingActionButtonTheme: const FloatingActionButtonThemeData(
    backgroundColor: primaryColor,
  ),
);
