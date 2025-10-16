
class Recipe {
  final int id;
  final String title;
  final String? description;
  final String? instructions;

  Recipe({
    required this.id,
    required this.title,
    this.description,
    this.instructions,
  });

  factory Recipe.fromJson(Map<String, dynamic> json) {
    return Recipe(
      id: json['id'],
      title: json['title'],
      description: json['description'],
      instructions: json['instructions'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'instructions': instructions,
    };
  }
}
