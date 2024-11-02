from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data produk peternakan dengan detail lengkap
products = [
    {"id": 1, "name": "Susu Sapi", "price": 15000, "stock": 20, "description": "Susu sapi segar murni dari peternakan"},
    {"id": 2, "name": "Telur Ayam", "price": 2000, "stock": 100, "description": "Telur ayam kampung, kaya protein"},
    {"id": 3, "name": "Daging Sapi", "price": 120000, "stock": 15, "description": "Daging sapi segar, dipotong setiap hari"},
    {"id": 4, "name": "Daging Ayam", "price": 35000, "stock": 30, "description": "Daging ayam segar, bebas antibiotik"},
    {"id": 5, "name": "Madu Asli", "price": 75000, "stock": 25, "description": "Madu asli tanpa campuran, dari lebah liar"},
    {"id": 6, "name": "Keju Sapi", "price": 50000, "stock": 10, "description": "Keju homemade dari susu sapi segar"},
    {"id": 7, "name": "Sosis Sapi", "price": 25000, "stock": 40, "description": "Sosis sapi segar tanpa bahan pengawet"},
    {"id": 8, "name": "Yogurt Sapi", "price": 20000, "stock": 18, "description": "Yogurt segar rendah lemak"},
    {"id": 9, "name": "Telur Bebek", "price": 2500, "stock": 60, "description": "Telur bebek organik kaya omega-3"},
    {"id": 10, "name": "Daging Kambing", "price": 130000, "stock": 12, "description": "Daging kambing segar, cocok untuk berbagai masakan"},
    {"id": 11, "name": "Susu Kambing", "price": 25000, "stock": 15, "description": "Susu kambing segar, kaya nutrisi"},
    {"id": 12, "name": "Susu Sapi Pasteurisasi", "price": 20000, "stock": 25, "description": "Susu sapi segar yang sudah dipasteurisasi"},
    {"id": 13, "name": "Butter", "price": 45000, "stock": 20, "description": "Butter homemade dari krim sapi"},
    {"id": 14, "name": "Kefir", "price": 35000, "stock": 15, "description": "Minuman kefir fermentasi yang baik untuk pencernaan"},
    {"id": 15, "name": "Telur Puyuh", "price": 1500, "stock": 80, "description": "Telur puyuh organik yang kaya nutrisi"},
]

class ProductList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(products),
            "products": products
        }

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return {
                "error": False,
                "message": "success",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(products) + 1,
            "name": data.get("name"),
            "price": data.get("price"),
            "stock": data.get("stock"),
            "description": data.get("description"),
        }
        products.append(new_product)
        return {
            "error": False,
            "message": "Product added successfully",
            "product": new_product
        }, 201

class UpdateProduct(Resource):
    def put(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return {"error": True, "message": "Product not found"}, 404

        data = request.get_json()
        product["name"] = data.get("name", product["name"])
        product["price"] = data.get("price", product["price"])
        product["stock"] = data.get("stock", product["stock"])
        product["description"] = data.get("description", product["description"])
        
        return {
            "error": False,
            "message": "Product updated successfully",
            "product": product
        }

class DeleteProduct(Resource):
    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]
        return {"error": False, "message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<int:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<int:product_id>')

if __name__ == "__main__":
    app.run(debug=True)
