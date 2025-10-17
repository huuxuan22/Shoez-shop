import { ref, computed } from 'vue';

export function useProductFilters(products) {
    // Filters state
    const filters = ref({
        search: '',
        brands: [],
        categories: [],
        colors: [],
        sizes: [],
        priceRange: [0, 10000000]
    });

    // Sort state
    const sortBy = ref('default');

    // Filtered products
    const filteredProducts = computed(() => {
        return products.value.filter(product => {
            // Search filter
            if (filters.value.search && !product.name.toLowerCase().includes(filters.value.search.toLowerCase())) {
                return false;
            }

            // Brand filter
            if (filters.value.brands.length > 0 && !filters.value.brands.includes(product.brand)) {
                return false;
            }

            // Category filter
            if (filters.value.categories.length > 0 && !filters.value.categories.includes(product.category)) {
                return false;
            }

            // Color filter
            if (filters.value.colors.length > 0) {
                const hasMatchingColor = product.colors.some(color =>
                    filters.value.colors.some(filterColor => color.includes(filterColor))
                );
                if (!hasMatchingColor) return false;
            }

            // Size filter
            if (filters.value.sizes.length > 0) {
                const hasMatchingSize = product.sizes.some(size => filters.value.sizes.includes(size));
                if (!hasMatchingSize) return false;
            }

            // Price range filter
            if (product.price < filters.value.priceRange[0] || product.price > filters.value.priceRange[1]) {
                return false;
            }

            return true;
        });
    });

    // Sorted products
    const sortedProducts = computed(() => {
        const products = [...filteredProducts.value];

        switch (sortBy.value) {
            case 'price-asc':
                return products.sort((a, b) => a.price - b.price);
            case 'price-desc':
                return products.sort((a, b) => b.price - a.price);
            case 'name-asc':
                return products.sort((a, b) => a.name.localeCompare(b.name));
            case 'name-desc':
                return products.sort((a, b) => b.name.localeCompare(a.name));
            default:
                return products;
        }
    });

    // Clear all filters
    const clearFilters = () => {
        filters.value = {
            search: '',
            brands: [],
            categories: [],
            colors: [],
            priceRange: [0, 10000000]
        };
        sortBy.value = 'default';
    };

    // Set initial filter from URL params
    const setInitialFilters = (queryParams) => {
        if (queryParams.brand) {
            filters.value.brands = [queryParams.brand];
        }
    };

    return {
        filters,
        sortBy,
        filteredProducts,
        sortedProducts,
        clearFilters,
        setInitialFilters
    };
}
