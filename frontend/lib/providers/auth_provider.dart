
import 'package:flutter/material.dart';
import 'package:recipe_genie_frontend/models/user.dart';
import 'package:recipe_genie_frontend/services/auth_service.dart';

class AuthProvider with ChangeNotifier {
  final AuthService _authService = AuthService();
  User? _user;
  bool _isLoading = false;

  User? get user => _user;
  bool get isLoading => _isLoading;

  AuthProvider() {
    fetchUser();
  }

  Future<void> fetchUser() async {
    _isLoading = true;
    notifyListeners();
    _user = await _authService.fetchUser();
    _isLoading = false;
    notifyListeners();
  }

  Future<void> login() async {
    await _authService.login();
  }

  Future<void> logout() async {
    await _authService.logout();
    _user = null;
    notifyListeners();
  }
}
