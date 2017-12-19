import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkSgIseComponent } from './link-sg-ise.component';

describe('LinkSgIseComponent', () => {
  let component: LinkSgIseComponent;
  let fixture: ComponentFixture<LinkSgIseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LinkSgIseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LinkSgIseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
