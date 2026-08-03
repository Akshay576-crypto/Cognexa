import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import WhoWeAre from "../components/WhoWeAre";
import Problem from "../components/Problem";

function Index() {
    return (
        <main className="min-h-screen bg-black">
            <Navbar />

            <Hero />

            <WhoWeAre />

            <Problem />

            <section
                id="platform"
                className="min-h-[400px] bg-black px-6 py-32 text-center"
            >
                <p className="text-sm uppercase tracking-[0.25em] text-white/30">
                    Cognexa Platform
                </p>

                <h2 className="mt-4 text-4xl font-semibold text-white">
                    Intelligence beyond information.
                </h2>
            </section>
        </main>
    );
}

export default Index;