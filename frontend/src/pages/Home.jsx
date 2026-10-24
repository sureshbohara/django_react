import BannerSection from '@/components/home/BannerSection';
import TrustBar from '@/components/home/TrustBar';
import InfoSection from '@/components/home/InfoSection';
import CategorySection from '@/components/home/CategorySection';
import BrandSection from '@/components/home/BrandSection';
import ProductCarousel from '@/components/home/ProductCarousel';
import FlashSaleSection from '@/components/home/FlashSaleSection';
import PromoBanner from '@/components/home/PromoBanner';
import ReviewSection from '@/components/home/ReviewSection';
import ServiceSection from '@/components/home/ServiceSection';
import InstagramSection from '@/components/home/InstagramSection';
import BlogSection from '@/components/home/BlogSection';

export default function Home() {
  return (
    <>
      <BannerSection />
      <TrustBar />
      <InfoSection />
      <CategorySection />
      <BrandSection />
      <ProductCarousel />
      <FlashSaleSection />
      <PromoBanner />
      <ReviewSection />
      <ServiceSection />
      <InstagramSection />
      <BlogSection />
    </>
  );
}