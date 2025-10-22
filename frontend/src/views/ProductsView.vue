<template>
  <div>
    <h2>Products</h2>
    <p>Inventory ID: {{ INVENTORY_ID }}</p>

    <div v-if="loadingError" class="alert alert-danger">Nepodařilo se načíst produkty.</div>

    <div v-if="backendLoading" class="alert alert-warning">Probíhá startování backend služby.</div>

    <div v-if="!loadingError && !backendLoading">
      <table class="table table-striped table-bordered table-hover">
        <thead class="table-dark">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">SKU</th>
            <th scope="col">EAN</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Extra Field 1</th>
            <th scope="col">Extra Field 2</th>
            <th scope="col">Akce</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.sku }}</td>
            <td>{{ product.ean }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.extra_field_1 }}</td>
            <td>
              <div v-if="showEditFieldId === product.id">
                <input type="text" v-model="editedFieldsValue[product.id]" />
                <button type="button" @click="saveEdit(product.id)" class="btn btn-secondary ms-2">
                  Uložit
                </button>
                <button type="button" @click="cancelEdit" class="btn btn-secondary ms-2">
                  Zrušit
                </button>
              </div>
              <div v-else>{{ product.extra_field_2 }}</div>
            </td>
            <td>
              <button type="button" @click="showEditFieldClick(product.id)" class="btn btn-secondary ms-2">
                Upravit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// References
const INVENTORY_ID = 833
const backendLoading = ref(true)
const loadingError = ref(null)
const products = ref([])
const showEditFieldId = ref(null)
const editedFieldsValue = ref({})

// Init page load
onMounted(async () => {
  startBackendService()
})

const startBackendService = async () => {
  const response = await fetch('/api/health')
  if (response.status == 200) {
    backendLoading.value = false
    loadProducts(INVENTORY_ID)
  }
  else {
    loadingError.value = 'Nepodařilo se načíst backend službu.'
  }
}

// Products
const loadProducts = async (inventoryId) => {
  const response = await fetch(`/api/inventory-products/${inventoryId}`)
  if (response.status != 200) {
    loadingError.value = 'Nepodařilo se načíst produkty.'
    return;
  }
  const result = await response.json()
  products.value = result
}

const showEditFieldClick = (productId) => {
  showEditFieldId.value = productId
  const product = products.value.find((p) => p.id === productId)
  editedFieldsValue.value[productId] = product?.extra_field_2 || ''
}

const saveEdit = async (productId) => {
  const index = products.value.findIndex((p) => p.id === productId)
  if (index !== -1) {
    // Get value
    const newValue = editedFieldsValue.value[productId]
    // Send to server
    const payload = { inventory_id: INVENTORY_ID, product_id: productId, extra_field_2: newValue }
    const response = await fetch('/api/products', {
      method: 'PUT',
      body: JSON.stringify(payload),
      headers: { 'Content-Type': 'application/json' },
    })
    if (response.status !== 200) {
      const error = await response.text()
      alert(`Nepodařilo se aktualizovat pole. Chyba ${response.status}: ${error}`)
      return;
    }
    // Update locally
    products.value[index].extra_field_2 = newValue
  }
  showEditFieldId.value = null
}

const cancelEdit = () => {
  showEditFieldId.value = null
}
</script>

<style scoped></style>
