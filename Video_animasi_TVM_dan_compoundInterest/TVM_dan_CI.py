from manim import *

class Awalan(Scene):
    def construct(self):
        text_1 = Tex("Compound Interest (Bunga Majemuk)").scale(1)
        text_2 = Tex("Warren Buffet", "Timothy Ronald").scale(1)
        text_3 = Tex("Simple vs Compound ").scale(1)
        animasi = [
            FadeIn(text_2[0].move_to(LEFT * 3)),
            FadeIn(text_2[1].move_to(RIGHT * 3))
        ]
        self.play(FadeIn(text_1))
        self.wait(3)
        self.play(FadeOut(text_1))
        self.play(AnimationGroup(*animasi, lag_ratio=0.5))
        self.wait(3)
        self.play(FadeOut(text_2))
        self.play(FadeIn(text_3))
        self.wait(1.5)



class Introduction(Scene):
    def construct(self):
        logo = ImageMobject("asset/logo.png")
        logo.scale(1.5)            # opsional: perbesar sedikit
        self.play(FadeIn(logo))    # fade in logo
        self.wait(2)

class EllipseBubble(VGroup):
    def __init__(self, text, scale=0.3, **kwargs):
        super().__init__(**kwargs)

        # Bubble utama bentuk elips
        bubble = Ellipse(width=3, height=1.5, color=WHITE).set_fill(BLACK, opacity=1)

        # Teks di dalam bubble
        bubble_text = Text(text).scale(scale)
        bubble_text.move_to(bubble.get_center())

        # "Ekor" bubble: titik kecil
        tail = Circle(radius=0.15, color=WHITE).set_fill(BLACK, opacity=1)

        # Grouping
        self.add(bubble, tail, bubble_text)

    def point_tail_to(self, target, buff=0.3):
        """
        Mengatur posisi 'ekor' bubble supaya mengarah ke sebuah objek
        """
        # Posisi target
        direction = (target.get_center() - self.get_center())

        # Tempatkan bubble (ellipse) tetap, geser tail-nya
        self[1].move_to(self.get_center() + direction * 0.45)  # ekor kecil
        return self




class PerbandinganDO(Scene):
    def ganti_tex(self, mobject, new_text):
        new_obj = MathTex(new_text).move_to(mobject)
        return new_obj
    
    def construct(self):
        #object emote
        jojo = SVGMobject("asset/jojo.svg").scale(0.8).move_to(LEFT*3)
        khohar = SVGMobject("asset/Khohar.svg").scale(0.8).move_to(RIGHT*3)
        #object nama
        namaJojo = Text("Jojo").scale(0.5)
        namaKhohar = Text("Khohar").scale(0.5)
        
        namaJojo.next_to(jojo, UP)
        namaKhohar.next_to(khohar, UP)
        #object uang
        uang1 = SVGMobject("asset/uang.svg").scale(0.5)
        uang2 = SVGMobject("asset/uang.svg").scale(0.5)

        uang1.next_to(jojo, RIGHT)
        uang2.next_to(khohar, LEFT)
        #uang text
        uangText1 = Text("+ 1.000.000").scale(0.5)
        uangText2 = Text("+ 1.000.000").scale(0.5)

        uangText1.next_to(namaJojo, UP * 1.5)
        uangText2.next_to(namaKhohar, UP * 1.5)

        #object perhitungan
        rumusJojo = MathTex("A ", "= ", "P ", r" \times ", r"(1 + ", "r ", r" \times ", "t ",")")

        # Animasi
        self.play(FadeIn(jojo), FadeIn(namaJojo))
        self.play(FadeIn(khohar), FadeIn(namaKhohar))
        self.play(FadeIn(uang1), FadeIn(uang2), run_time=0.5)
        self.play(FadeIn(uangText1), FadeIn(uangText2), run_time=0.5)

        self.wait(5)

        self.play(
            FadeOut(jojo), FadeOut(namaJojo),
            FadeOut(khohar), FadeOut(namaKhohar),
            FadeOut(uang1), FadeOut(uang2),
            FadeOut(uangText1), FadeOut(uangText2)
        )

        self.wait(0.5)

        bisnisJojo = SVGMobject("asset/bisnis.svg").scale(1.3).move_to(RIGHT * 3)
        uang1.next_to(jojo, RIGHT)
        uangText1.next_to(bisnisJojo, UP)
        
        self.play(
            FadeIn(jojo), FadeIn(uang1), 
            FadeIn(bisnisJojo), FadeIn(namaJojo)
        )
        # animasi
        self.play(uang1.animate.move_to(RIGHT * 1.4), run_time=1.5)
        self.play(FadeIn(uangText1, shift = DOWN, run_time = 0.5))
        self.wait(2)

        bubble1 = EllipseBubble("Nih, sejuta!").next_to(jojo, DOWN)
        bubble1.point_tail_to(jojo)  # arahkan ekor ke Jojo
        self.play(FadeIn(bubble1))
        self.wait(1)
        self.play(FadeOut(bubble1))

        bubble2 = EllipseBubble("Kamu dapet bunga 50%/tahun ya", scale=0.28).next_to(bisnisJojo, DOWN)
        bubble2.point_tail_to(bisnisJojo)
        self.play(FadeIn(bubble2))
        self.wait(1)
        self.play(FadeOut(bubble2))


        self.play(
            FadeOut(uangText1), FadeOut(bisnisJojo),
            FadeOut(uang1)
        )

        rumusJojo.move_to(RIGHT * 2)
        self.play(
            Write(rumusJojo)
        )
        framebox1 = SurroundingRectangle(rumusJojo[0], buff = .1)
        framebox2 = SurroundingRectangle(rumusJojo[2], buff = .1)
        framebox3 = SurroundingRectangle(rumusJojo[5], buff = .1)
        framebox4 = SurroundingRectangle(rumusJojo[7], buff = .1)

        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2)
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox2,framebox3)
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox3,framebox4)
        )
        self.play(Uncreate(framebox4))
        self.wait(1.5)

        #perhitungan
        rumusBaru1= MathTex(
            "A", "=", "1.000.000", r"\times", r"(1 + 0.5 \times 1)"
        ).move_to(rumusJojo)
        rumusBaru2 = MathTex(
            "A", "=", "1.500.000"
        ).move_to(rumusJojo)
        rumusBaru3 = MathTex(
            "A = ", "1.500.000, ", "2.000.000, ", "2.500.000", "..."
        ).move_to(rumusJojo)

        # Sembunyikan dulu elemen ke-1 sampai akhir
        for i in range(1, len(rumusBaru3)):
            rumusBaru3[i].set_opacity(0)

        # transform tahap sebelumnya
        self.play(TransformMatchingTex(rumusJojo, rumusBaru1))
        self.play(TransformMatchingTex(rumusBaru1, rumusBaru2))
        jojoGroup = VGroup(jojo, namaJojo)
        self.play(jojoGroup.animate.move_to(LEFT * 3.75))


        # transform ke rumusBaru3 (hanya A= yang kelihatan)
        self.play(TransformMatchingTex(rumusBaru2, rumusBaru3), run_time=1.5)

        # munculkan angka satu per satu
        self.play(FadeIn(rumusBaru3[1].set_opacity(1), shift=UP), run_time=0.8)
        self.play(FadeIn(rumusBaru3[2].set_opacity(1), shift=UP), run_time=0.8)
        self.play(FadeIn(rumusBaru3[3].set_opacity(1), shift=UP), run_time=0.8)
        self.play(FadeIn(rumusBaru3[4].set_opacity(1), shift=UP), run_time=0.8)
        


        
