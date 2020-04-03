from manimlib.imports import *

class L2(Scene):
    def construct(self):
        Main_text = TexMobject(
            "\\lim_{x\\rightarrow0}",
            "{{\\left(\\frac{\\tan{x}}{x}\\right)}",
            "^",
            "{\\frac{1}{x}}}")
        self.play(Write(Main_text))
        self.wait()
        self.play(
            Main_text.shift, 3*UP,            
        )
        self.wait(2)
        r_arrow = TexMobject("as\\ ","x\\rightarrow","0",",")
        r_arrow.next_to(Main_text,DOWN,0.5,aligned_edge=LEFT)
        r_arrow.next_to(r_arrow,LEFT)
        self.play(Write(r_arrow))
        self.wait()
        lim1 = TexMobject("{{\\left(\\tan{x}\\over{x}\\right)}")
        lim1.next_to(r_arrow,RIGHT,2.5)
        self.play(Write(lim1))
        self.wait()
        r_arrow_2=TexMobject("\\rightarrow"," 1")
        r_arrow_2.next_to(lim1,RIGHT)
        self.play(Write(r_arrow_2))
        self.wait()
        one_by_x = TexMobject(" { 1","\\over", "x }")
        one_by_x.next_to(lim1,DOWN,buff=0.5,aligned_edge=LEFT)
        one_by_x.next_to(one_by_x,RIGHT,buff=0.1)
        self.play(Write(one_by_x))#6
        self.wait()
        clone =TexMobject(" { 1","\\over", "0}")
        clone.next_to(lim1,DOWN,0.5)
        self.play(
            Transform(one_by_x,clone),
            ReplacementTransform(r_arrow[2].copy(),clone[2]))
        self.wait()
        r_arrow3=TexMobject("\\rightarrow","\\infty")
        r_arrow3.next_to(clone,RIGHT)
        self.play(Write(r_arrow3))
        self.wait()
        equals = TextMobject("=")
        equals.next_to(Main_text,RIGHT,0.5)
        rhs_transform = TexMobject("{ 1 }","^","{ \\infty  }")
        rhs_transform.next_to(Main_text,RIGHT,1.5,aligned_edge=RIGHT)
        self.play(Write(equals))#7
        self.play(Transform(r_arrow_2[1].copy(),rhs_transform[0]))#8
        self.play(Transform(r_arrow3[1].copy(),rhs_transform[2]))#9
        self.wait()
        step_1=TexMobject(
            "\\log",
            "y",
            "=",#2
            "{1\\over x}",
            "\\log",
            "{{\\left(\\frac{\\tan{x}}{x}\\right)}",
            "^",
            "{1\\over x}"
        )
        step_1.shift(1.5*DOWN)
        self.play(
            Write(step_1[0:3]),
            Write(step_1[4:8])
                )
        self.wait()
        self.play(ReplacementTransform(step_1[7],step_1[3]))
        self.wait()
        self.play(*[FadeOut(x) for x in self.mobjects],run_time=0.001)
        self.play(step_1.shift,4.5*UP)
        self.wait()
        step_2=TexMobject(
            "\\log y=",
            "{\\left({\\tan{x} \\over x}}\\right)",
            "\\over",
            "x}"
            )
        step_2.next_to(step_1,DOWN,0.5)
        self.wait()
        step_3 = TexMobject(
            "\\log y =",
            "{(\\log{\\tan{x}}-\\log{x}) \\over {x}"
        )
        step_3.next_to(step_2,DOWN,0.5)
        self.play(Write(step_3))
        self.wait()
        step_4 = TexMobject(
            "\\lim_{x\\rightarrow0}",
            "{(\\log{\\tan{x}}-\\log{x}) \\over {x}"
        )
        step_4.next_to(step_3,DOWN,0.5)
        self.play(Write(step_4))
        self.play(*[FadeOut(x) for x in self.mobjects],run_time=0.001)
        self.play(step_4.shift,4.5*UP)
        self.wait()
        r1_arrow = TexMobject(
            "as\\ ",
            "x\\rightarrow",
            "0"
            ",")
        r1_arrow.next_to(Main_text,DOWN,1)
        r1_arrow.next_to(r1_arrow,LEFT)
        self.play(Write(r1_arrow))#3
        self.wait()
        lim_2 = TexMobject(
            "(",
            "\\log{\\tan",
            "{x}}",
            "-",
            "\\log{x}",
            ")"
        )
        lim_2.next_to(r1_arrow,RIGHT,2)
        self.play(Write(lim_2))
        self.wait()
        clone_lim_2 = TexMobject(
            "(",
            "\\log{\\tan",
            "{0}}",
            "-",
            "\\log{0}",
            ")"
        )
        clone_lim_2.next_to(r1_arrow,RIGHT,2)
        self.play(
            Transform(lim_2,clone_lim_2),
            ReplacementTransform(r1_arrow[2].copy(),clone_lim_2[2]),
            ReplacementTransform(r1_arrow[2].copy(),clone_lim_2[4])
            )
        self.wait()
        r2_arrow = TexMobject("\\rightarrow","0")
        r2_arrow.next_to(clone_lim_2,RIGHT)
        self.play(Write(r2_arrow))
        self.wait()
        r2_arrow_x = TexMobject(
            "x\\rightarrow",
            "0"
        )
        r2_arrow_x.next_to(clone_lim_2,DOWN,0.5,aligned_edge=LEFT)
        self.play(Write(r2_arrow_x))
        self.wait()
        rhs_transform1 = TexMobject("=","{0","\\over","0}")
        rhs_transform1.next_to(step_4,RIGHT)
        self.play(
            Write(rhs_transform1[0]),
            Write(rhs_transform1[2]),
            Transform(r2_arrow[1].copy(),rhs_transform1[1]),
            Transform(r2_arrow_x[1].copy(),rhs_transform1[3]),
            run_time=3
            )#7
        self.wait()
        LH = TextMobject("L'Hospital Rule")
        LH.shift(2*LEFT+0.5*DOWN)
        self.play(Write(LH))
        self.wait()
        cl_1 = copy.deepcopy(step_4)
        cl_1.next_to(LH,DOWN)
        self.play(Write(cl_1))
        self.wait()
        LH_step_1 = TexMobject(
          "=\\lim _{x\\rightarrow0}{\\frac{\\frac{d}{dx}\\left(\log{\\left(\\tan{x}\\right)}-\\log{x}\\right)}{\\frac{d}{dx}(x)}}"
        )
        LH_step_1.next_to(cl_1,RIGHT,0.5)
        self.play(Write(LH_step_1))
        self.wait()