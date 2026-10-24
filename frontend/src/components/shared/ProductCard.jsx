import { Link } from 'react-router-dom';
import { addToCart } from '@/services/api';

export default function ProductCard({ product, isFlashSale = false }) {
  const handleAddToCart = async (e) => {
    e.preventDefault();
    try {
      await addToCart({ product_id: product.id, quantity: 1 });
    } catch (error) {}
  };

  const cardStyle = isFlashSale ? { background: 'rgba(255,255,255,0.05)', borderColor: 'rgba(197,160,89,0.25)' } : {};
  const titleStyle = isFlashSale ? { color: 'var(--bg-white)' } : {};
  const priceStyle = isFlashSale ? { color: 'var(--accent-color)' } : {};
  const oldPriceStyle = isFlashSale ? { color: 'rgba(255,255,255,0.5)' } : {};
  const btnStyle = isFlashSale ? { background: 'var(--accent-color)', color: 'var(--bg-white)', borderColor: 'var(--accent-color)' } : {};

  return (
    <div className="product-card" style={cardStyle}>
      <div className="img-wrapper">
        {product.is_on_sale && <span className="product-badge">Sale</span>}
        <Link to={`/products/${product.slug}`}>
          <img src={product.thumbnail_url} alt={product.name} />
        </Link>
      </div>
      <h3 style={titleStyle}>{product.name}</h3>
      <div className="price-wrap">
        <span className="current-price" style={priceStyle}>Rs. {product.final_price}</span>
        {product.is_on_sale && <span className="original-price" style={oldPriceStyle}>Rs. {product.regular_price}</span>}
      </div>
      <button className="add_to_cart" style={btnStyle} onClick={handleAddToCart}>
        <i className="bi bi-bag-plus"></i> Add To Cart
      </button>
    </div>
  );
}