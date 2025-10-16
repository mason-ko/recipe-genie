
import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:http/http.dart' as http;

class RecipeService {
  final String? _baseUrl = dotenv.env['API_URL'];

  Future<List<dynamic>> getRecipes() async {
    if (_baseUrl == null) {
      throw Exception('API_URL not found in .env file');
    }
    final response = await http.get(Uri.parse('$_baseUrl/recipes/'));

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load recipes');
    }
  }

  Future<dynamic> generateRecipe(List<String> ingredients) async {
    if (_baseUrl == null) {
      throw Exception('API_URL not found in .env file');
    }
    final response = await http.post(
      Uri.parse('$_baseUrl/recipes/generate'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'ingredients': ingredients}),
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to generate recipe');
    }
  }
}
