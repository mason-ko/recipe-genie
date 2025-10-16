
class User {
  final String id;
  final String email;
  final String? name;
  final String? picture;

  User({
    required this.id,
    required this.email,
    this.name,
    this.picture,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      email: json['email'],
      name: json['name'],
      picture: json['picture'],
    );
  }
}
