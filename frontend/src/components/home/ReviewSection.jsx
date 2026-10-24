import { useState, useEffect } from 'react';
import { fetchReviews } from '@/services/api';

export default function ReviewSection() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetchReviews().then(setReviews).catch(console.error);
  }, []);

  return (
    <section className="review-section section">
      <div className="container">
        <div className="review-header">
          <h2 className="review-title">What Our Clients Say</h2>
          <p style={{ opacity: 0.8 }}>from <span className="review-count"> {reviews.length}+ </span> verified reviews</p>
        </div>
        <div className="react-carousel carousel-multi">
          {reviews.length > 0 ? reviews.map(review => (
            <div key={review.id} className="review-card">
              <div className="review-card__header">
                <div className="review-card__user">
                  <div className="review-card__avatar">{review.name?.charAt(0) || 'U'}</div>
                  <div>
                    <h4 className="review-card__name">{review.name}</h4>
                    <span className="review-card__badge"><i className="bi bi-patch-check-fill"></i> Verified Buyer</span>
                  </div>
                </div>
                <div className="review-card__stars">{'★'.repeat(review.rating)}</div>
              </div>
              <p className="review-card__text">"{review.review}"</p>
            </div>
          )) : (
            <p className="text-center text-white">No reviews yet.</p>
          )}
        </div>
      </div>
    </section>
  );
}