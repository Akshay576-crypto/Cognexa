import { useEffect, useRef, useState } from "react";
import "./CognexaScrollStage.css";

const layers = [
    {
        id: "documents",
        number: "01",
        title: "Documents",
        subtitle: "Raw information",
        description: "Unstructured information enters the Cognexa intelligence layer.",
    },
    {
        id: "hac",
        number: "02",
        title: "HAC",
        subtitle: "Adaptive chunking",
        description: "Structure is understood before information is segmented.",
    },
    {
        id: "embeddings",
        number: "03",
        title: "Embeddings",
        subtitle: "Semantic representation",
        description: "Meaning is transformed into a representation machines can understand.",
    },
    {
        id: "vector",
        number: "04",
        title: "Vector Space",
        subtitle: "Meaning encoded",
        description: "Related information becomes connected through semantic space.",
    },
    {
        id: "hare",
        number: "05",
        title: "HARE",
        subtitle: "Adaptive retrieval",
        description: "The right context is retrieved when intelligence needs it.",
    },
];

function CognexaScrollStage() {
    const stageRef = useRef(null);
    const [progress, setProgress] = useState(0);

    useEffect(() => {
        const updateProgress = () => {
            const element = stageRef.current;

            if (!element) return;

            const rect = element.getBoundingClientRect();
            const scrollable = element.offsetHeight - window.innerHeight;

            if (scrollable <= 0) return;

            const value = Math.min(
                1,
                Math.max(0, -rect.top / scrollable)
            );

            setProgress(value);
        };

        updateProgress();

        window.addEventListener("scroll", updateProgress, {
            passive: true,
        });

        window.addEventListener("resize", updateProgress);

        return () => {
            window.removeEventListener("scroll", updateProgress);
            window.removeEventListener("resize", updateProgress);
        };
    }, []);

    const activeIndex = Math.min(
        layers.length - 1,
        Math.floor(progress * layers.length)
    );

    return (
        <section
            ref={stageRef}
            className="cognexa-scroll-stage"
        >
            <div className="cognexa-scroll-sticky">

                {/* Ambient environment */}
                <div className="scroll-orb scroll-orb-violet" />
                <div className="scroll-orb scroll-orb-cyan" />

                {/* Header */}
                <div className="scroll-stage-label">
                    <span>COGNEXA</span>
                    <span>INTELLIGENCE LAYER</span>
                </div>

                {/* Central C */}
                <div className="scroll-core">
                    <div className="scroll-core-ring" />

                    <span className="scroll-core-letter">
                        C
                    </span>

                    <span className="scroll-core-caption">
                        intelligence
                    </span>
                </div>

                {/* Layer cards */}
                <div className="scroll-layer-space">
                    {layers.map((layer, index) => {
                        const distance = index - progress * (layers.length - 1);

                        const translateY = distance * 150;
                        const scale = Math.max(
                            0.72,
                            1 - Math.abs(distance) * 0.12
                        );

                        const opacity = Math.max(
                            0.12,
                            1 - Math.abs(distance) * 0.48
                        );

                        const rotateX = distance * -18;

                        const zIndex =
                            100 - Math.round(Math.abs(distance) * 10);

                        return (
                            <article
                                key={layer.id}
                                className={`scroll-layer-card ${index === activeIndex
                                        ? "is-active"
                                        : ""
                                    }`}
                                style={{
                                    transform: `
                                        translate3d(
                                            0,
                                            ${translateY}px,
                                            0
                                        )
                                        perspective(900px)
                                        rotateX(${rotateX}deg)
                                        scale(${scale})
                                    `,
                                    opacity,
                                    zIndex,
                                }}
                            >
                                <div className="scroll-card-reflection" />

                                <div className="scroll-card-top">
                                    <span>{layer.number}</span>

                                    <span className="scroll-card-status">
                                        {index === activeIndex
                                            ? "ACTIVE"
                                            : "LAYER"}
                                    </span>
                                </div>

                                <div className="scroll-card-content">
                                    <p>{layer.subtitle}</p>

                                    <h2>{layer.title}</h2>

                                    <span>
                                        {layer.description}
                                    </span>
                                </div>

                                <div className="scroll-card-line" />
                            </article>
                        );
                    })}
                </div>

                {/* Progress */}
                <div className="scroll-progress">
                    {layers.map((layer, index) => (
                        <span
                            key={layer.id}
                            className={
                                index === activeIndex
                                    ? "active"
                                    : ""
                            }
                        />
                    ))}
                </div>

                <div className="scroll-hint">
                    SCROLL TO EXPLORE
                </div>
            </div>
        </section>
    );
}

export default CognexaScrollStage;