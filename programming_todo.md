I am trying to get my carousel to work again by being like the cafe brazil webpage.
I am trying to get my Bootstrapped navbar to have the django hyperlinks apply to it. 

keeping here this just in case
      {% comment %} <!-- the green text is talking about paths the white is what is on the page-->
      {% comment %} <a href="{% url 'home' %}">Home</a>
      <a href="{% url 'ingredients' %}">Ingredients</a>
      <!-- name= connection-->
      <a href="{% url 'menu' %}">Menu</a>
      <a href="{% url 'finance' %}">Finance</a>
      <a href="{% url 'purchases' %}">Purchases</a>
      <a href="{% url 'menuadd' %}">Add Menu</a>
      <!--utilize name in urls.py -->
      <a href="{% url 'ingredientadd' %}">Add Ingredient</a>
      <a href="{% url 'recipeadd' %}">Add Recipe</a>
      <a href="{% url 'purchaseadd' %}">Add Purchase</a> {% endcomment %}
      {# <a href="{% url 'ingredientupdate' object.pk %}">Ingredient Update</a> #} 
