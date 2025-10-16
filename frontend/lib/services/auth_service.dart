
import 'dart:convert';

import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:http/http.dart' as http;
import 'package:recipe_genie_frontend/models/user.dart';
import 'package:url_launcher/url_launcher.dart';

class AuthService {
  final String? _baseUrl = dotenv.env['API_URL'];

  Future<void> login() async {
    if (_baseUrl == null) {
      throw Exception('API_URL not found in .env file');
    }
    final url = Uri.parse('$_baseUrl/auth/login');
    if (await canLaunchUrl(url)) {
      await launchUrl(url, webOnlyWindowName: '_self');
    } else {
      throw 'Could not launch $url';
    }
  }

  Future<User?> fetchUser() async {
    if (_baseUrl == null) {
      return null;
    }
    final response = await http.get(Uri.parse('$_baseUrl/users/me'));

    if (response.statusCode == 200) {
      return User.fromJson(json.decode(response.body));
    } else {
      return null;
    }
  }

  Future<void> logout() async {
    if (_baseUrl == null) {
      return;
    }
    await http.post(Uri.parse('$_baseUrl/auth/logout'));
  }
}
