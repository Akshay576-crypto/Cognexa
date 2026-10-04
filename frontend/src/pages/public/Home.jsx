import Navbar from "../../components/layout/Navbar";

import Hero from "../../components/hero/Hero";
import WhatWeDo from "../../components/hero/WhatWeDo";
import WhoWeAre from "../../components/hero/WhoWeAre";

import HACSection from "../../components/hac/HACSection";
import HelixSection from "../../components/helix/HelixSection";

function Home() {
    return (
        <main className="min-h-screen bg-[#08090c] text-white">

            <Navbar />

            {/* Hero */}
            <Hero />

            {/* What Cognexa does */}
            <WhatWeDo />

            {/* Helix Adaptive Chunking */}
            <HACSection />

            {/* Who Cognexa is */}
            <WhoWeAre />

            {/* Cognexa Intelligence Engine */}
            <HelixSection />

        </main>
    );
}

export default Home;

